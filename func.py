```python
import io
import os
import json
import requests
import logging
from fdk import response


#This Function receives the Cloud Guard Problems and invokes the Splunk endpoint for ingesting the problems.
def handler(ctx, data: io.BytesIO = None):
    try:
        logs = json.loads(data.getvalue())
        events = logs.replace('\\n', '\n').replace('\\t', '\t')  # removes the \ and \n from the json dump
        

        # Splunk endpoint URL and token to call the HEC. These values are defined in func.yaml
        host = os.environ["Splunk_Hostname"]
        token = os.environ["HEC_Key"]
        payload = {"host": "OCI_Functions", "source": "Cloud_Guard", "event": json.dumps(events)}
        headers = {'Authorization': 'Splunk ' + token}
        x = requests.post(host, headers=headers, json=payload,verify=False)
        logging.getLogger().info(x.text)


    except (Exception, ValueError) as ex:
        logging.getLogger().info(str(ex))
        return
```
