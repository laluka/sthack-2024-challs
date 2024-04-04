# Do Your Updates Son

> I just set it up, it's up to date, but you don't know when I wrote this message, yesterday? Years ago? Hihi! :)

```bash
# Live Auto Fix
echo '*/30 * * * * root bash -c "cd /opt/sthack-2024-challs/do-your-updates-son ; docker compose run --rm -it --volume /opt/sthack-2024-challs/do-your-updates-son:/host -w /host --entrypoint /bin/bash mlflow -x exploit.sh ; docker compose down --remove-orphans --volumes ; docker compose up --build --remove-orphans -d"' | tee -a /etc/crontab
# Setup & Recheck
cd /opt/sthack-2024-challs/do-your-updates-son ; docker compose run --rm -it --volume "$PWD:/host" -w /host --entrypoint /bin/bash mlflow -x exploit.sh ; docker compose down --remove-orphans --volumes ; docker compose up --build --remove-orphans -d
# Logs
docker compose logs -f
# Doc / Source
# https://huntr.com/bounties/1fe8f21a-c438-4cba-9add-e8a5dab94e28
```
