# coding=utf-8
# *** WARNING: this file was generated by Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['K8sMonitorArgs', 'K8sMonitor']

@pulumi.input_type
class K8sMonitorArgs:
    def __init__(__self__, *,
                 api_key: pulumi.Input[str]):
        """
        The set of arguments for constructing a K8sMonitor resource.
        :param pulumi.Input[str] api_key: Datadog API key needed by k8s agent to communicate with Datadog
        """
        pulumi.set(__self__, "api_key", api_key)

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> pulumi.Input[str]:
        """
        Datadog API key needed by k8s agent to communicate with Datadog
        """
        return pulumi.get(self, "api_key")

    @api_key.setter
    def api_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "api_key", value)


class K8sMonitor(pulumi.ComponentResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_key: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a K8sMonitor resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_key: Datadog API key needed by k8s agent to communicate with Datadog
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: K8sMonitorArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a K8sMonitor resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param K8sMonitorArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(K8sMonitorArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_key: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is not None:
            raise ValueError('ComponentResource classes do not support opts.id')
        else:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = K8sMonitorArgs.__new__(K8sMonitorArgs)

            if api_key is None and not opts.urn:
                raise TypeError("Missing required property 'api_key'")
            __props__.__dict__["api_key"] = api_key
            __props__.__dict__["namespace"] = None
        super(K8sMonitor, __self__).__init__(
            'k8sdatadog:index:K8sMonitor',
            resource_name,
            __props__,
            opts,
            remote=True)

    @property
    @pulumi.getter
    def namespace(self) -> pulumi.Output[str]:
        """
        Namespace in which datadog agent is installed.
        """
        return pulumi.get(self, "namespace")

