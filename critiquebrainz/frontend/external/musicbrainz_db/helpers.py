import critiquebrainz.frontend.external.musicbrainz_db as mb
from critiquebrainz.utils import dict_uuids_to_str
import sqlalchemy


COLUMNS = {
    "artist-rels": {
        "artist": (
            "gid AS id",
            "name",
            "sort_name",
        ),
    },
    "place-rels": {
        "place": (
            "gid AS id",
            "name",
            "address",
            "coordinates",
        ),
    },
    "url-rels": {
        "url": (
            "url AS target",
        ),
    },
}


def entity_relation_helper(id, relation, *, relationship, entity_type,
                           is_linked_entity_first):
    """Get information related relationships between different entities

    Args:
        id(uuid): ID of the entity.
        relation(str): Type of relation-include. (url-rels, artist-rels, etc)
        relationship(str): The relationship table relating the two entities.
        entity_type(str): Type of the entity specified.
        is_linked_entity_first(bool): if true then the relationship table has relation table as the first entity.

    Returns:
        List of Dictionaries of related entities in the relationship.
    """
    relation_table = relation[:-5]
    columns = COLUMNS[relation][relation_table]
    query = """
        SELECT {columns},
               lt.name as link,
               lt.gid AS type_id,
               olt.direction
          FROM {relationship} r
    """.format(relationship=relationship, columns=", ".join(["a."+column for column in columns]))

    if is_linked_entity_first:
        query = query + """
            INNER JOIN {relation_table} a
                    ON a.id = r.entity0
            INNER JOIN {entity_table} e
                    ON r.entity1 = e.id
        """.format(entity_table=entity_type, relation_table=relation_table)
    else:
        query = query + """
            INNER JOIN {relation_table} a
                    ON a.id = r.entity1
            INNER JOIN {entity_table} e
                    ON r.entity0 = e.id
        """.format(entity_table=entity_type, relation_table=relation_table)

    query = query +  """
        INNER JOIN link l
                ON r.link = l.id
        INNER JOIN link_type lt
                ON l.link_type = lt.id
         LEFT JOIN orderable_link_type olt
                ON olt.link_type = lt.id
             WHERE e.gid = :id
    """
    with mb.engine.connect() as connection:
        result = connection.execute(sqlalchemy.text(query) ,{
                "id": id,
        })
        rows = result.fetchall()
    return [dict_uuids_to_str(dict(row)) for row in rows]
