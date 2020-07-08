#!/usr/bin/env python3

import config as cfg
import hvac

client_old = hvac.Client(url=cfg.old_url, token=cfg.old_token)
client_new = hvac.Client(url=cfg.new_url, token=cfg.new_token)

for secret in cfg.secrets:
    old_path = secret
    new_path = cfg.secrets[secret]
    data = client_old.read(secret).get('data')
    client_new.write(new_path, **data)
    print("Copied " + old_path + ' to ' + new_path)
