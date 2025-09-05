# this is the file that will be used to contain utility functions for the agents
import boto3
import json
import time
from datetime import datetime
from boto3.session import Session
import botocore
import requests
import os
import time
import logging
import yaml
from routing_rule import RoutingRule
from textwrap import wrap
from typing import Optional, Dict, Union, List, Tuple, Any
from pathlib import Path
from boto3.dynamodb.conditions import Attr
from botocore.exceptions import ClientError

# set a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Initialize S3 client
s3_client = boto3.client('s3')
# Initialize the bedrock runtime client. This is used to 
# query search results from the FMC and Meraki KBs
bedrock_agent_runtime_client = boto3.client('bedrock-agent-runtime') 


def load_config(config_file: Union[Path, str]) -> Optional[Dict]:
    """
    Load configuration from a local file.

    :param config_file: Path to the local file
    :return: Dictionary with the loaded configuration
    """
    try:
        config_data: Optional[Dict] = None
        logger.info(f"Loading config from local file system: {config_file}")
        content = Path(config_file).read_text()
        config_data = yaml.safe_load(content)
        logger.info(f"Loaded config from local file system: {config_data}")
    except Exception as e:
        logger.error(f"Error loading config from local file system: {e}")
        config_data = None
    return config_data

