ip_addr="$(ifconfig wlp4s0b1 | grep netmask | cut -d ' ' -f 10)"

if [ -z "$ip_addr" ]
then
    ip_addr="$(ifconfig enp3s0 | grep netmask | cut -d ' ' -f 10)"
fi

if [ -z "$ip_addr" ]
then
    echo "you seem not to be connected to some network. please connect and run script again"
else
    cd /home/ferbncode/code/critiquebrainz
    branch=$(git branch | sed -n -e 's/^\* \(.*\)/\1/p')
    echo "$branch is the current git branch you are running"
    echo "MB_DATABASE_URI = \"postgres://musicbrainz:musicbrainz@""$ip_addr"":5431/musicbrainz_db\""
    echo "MB_DATABASE_URI = \"postgres://musicbrainz:musicbrainz@""$ip_addr"":5431/musicbrainz_db\" " >> /home/ferbncode/code/critiquebrainz/default_config.py
    docker-compose -f /home/ferbncode/code/critiquebrainz/docker/docker-compose.dev.yml up
fi

