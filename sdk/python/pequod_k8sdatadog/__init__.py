# coding=utf-8
# *** WARNING: this file was generated by Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from . import _utilities
import typing
# Export this package's modules as members:
from .k8s_monitor import *
from .provider import *
_utilities.register(
    resource_modules="""
[
 {
  "pkg": "k8sdatadog",
  "mod": "index",
  "fqn": "pequod_k8sdatadog",
  "classes": {
   "k8sdatadog:index:K8sMonitor": "K8sMonitor"
  }
 }
]
""",
    resource_packages="""
[
 {
  "pkg": "k8sdatadog",
  "token": "pulumi:providers:k8sdatadog",
  "fqn": "pequod_k8sdatadog",
  "class": "Provider"
 }
]
"""
)
