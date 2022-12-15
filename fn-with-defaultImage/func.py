#
# oci-load-file-into-adw-python version 1.0.
#
# Copyright (c) 2020 Oracle, Inc.
# Licensed under the Universal Permissive License v 1.0 as shown at https://oss.oracle.com/licenses/upl.
#

import io
import json
import logging

from fdk import response


def handler(ctx, data: io.BytesIO=None):
    logging.getLogger().info("Invoked function with default  image")
    return response.Response(
        ctx, 
        response_data=json.dumps({"status": "Hello World! with DefaultImage"}),
        headers={"Content-Type": "application/json"}
    )
