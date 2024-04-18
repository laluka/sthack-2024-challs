# Stream Is Lit Isnt It

> TODO

- Medium / Web / Linux
- Sources are given
    - Remove the `Detail` from the readme
    - Censor the `flag_random_path` in `docker-compose.yml`
---

```bash
# Setup or Change Flag
sed -E 's#.*./flag:/flag/.*#      - ./flag:/flag/flag_random_path_plifplafplouf:ro#g' docker-compose.yml

# Setup & Recheck
cd /opt/sthack-2024-challs/stream-is-lit-isnt-it ; docker compose run --rm -it --volume "$PWD:/host" -w /host --entrypoint /bin/bash mlflow -x exploit.sh ; docker compose down --remove-orphans --volumes ; docker compose up --build --remove-orphans -d

# Logs
docker compose logs -f

# Light-Long Auto-Fix
echo '*/30 * * * * root bash -c "cd /opt/sthack-2024-challs/stream-is-lit-isnt-it ; docker compose run --rm -it --volume /opt/sthack-2024-challs/stream-is-lit-isnt-it:/host -w /host --entrypoint /bin/bash mlflow -x exploit.sh ; docker compose down --remove-orphans --volumes ; docker compose up --build --remove-orphans -d"' | sudo tee -a /etc/crontab

# Doc / Source
# TODO
```

# Detail

- Abust StreamLit for SSRF
- Abuse SSRF for Local File Read
- Read /proc/1/environ to get api_key
- Reuse api_key to cat flag
