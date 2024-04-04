# Do Your Updates Son

> I just set it up, it's up to date, but you don't know when I wrote this message. Yesterday? Years ago? Who knows!

- Medium / Web / Linux
- Sources are given

```bash
# Setup or Change Flag
sed -E 's#.*./flag:/flag/.*#      - ./flag:/flag/flag_random_path_plifplafplouf:ro#g' docker-compose.yml

# Setup & Recheck
cd /opt/sthack-2024-challs/do-your-updates-son ; docker compose run --rm -it --volume "$PWD:/host" -w /host --entrypoint /bin/bash mlflow -x exploit.sh ; docker compose down --remove-orphans --volumes ; docker compose up --build --remove-orphans -d

# Logs
docker compose logs -f

# Light-Long Auto-Fix
echo '*/30 * * * * root bash -c "cd /opt/sthack-2024-challs/do-your-updates-son ; docker compose run --rm -it --volume /opt/sthack-2024-challs/do-your-updates-son:/host -w /host --entrypoint /bin/bash mlflow -x exploit.sh ; docker compose down --remove-orphans --volumes ; docker compose up --build --remove-orphans -d"' | sudo tee -a /etc/crontab

# Doc / Source
# https://huntr.com/bounties/1fe8f21a-c438-4cba-9add-e8a5dab94e28
```

# Detail

- Abuse mlflow (see the nice huntrdev writeup from mizu)
- Read `/var/cache/locate/locatedb` and extract the flag path
- Read the flag with the same exploit
