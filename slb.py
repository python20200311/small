from aliyun import client, desc_it
from aliyunsdkslb.request.v20140515.AddAccessControlListEntryRequest import AddAccessControlListEntryRequest
from aliyunsdkslb.request.v20140515.AddBackendServersRequest import AddBackendServersRequest
from aliyunsdkslb.request.v20140515.AddListenerWhiteListItemRequest import AddListenerWhiteListItemRequest
from aliyunsdkslb.request.v20140515.AddTagsRequest import AddTagsRequest
from aliyunsdkslb.request.v20140515.AddVServerGroupBackendServersRequest import AddVServerGroupBackendServersRequest
from aliyunsdkslb.request.v20140515.CreateAccessControlListRequest import CreateAccessControlListRequest
from aliyunsdkslb.request.v20140515.CreateDomainExtensionRequest import CreateDomainExtensionRequest
from aliyunsdkslb.request.v20140515.CreateLoadBalancerHTTPListenerRequest import CreateLoadBalancerHTTPListenerRequest
from aliyunsdkslb.request.v20140515.CreateLoadBalancerHTTPSListenerRequest import CreateLoadBalancerHTTPSListenerRequest
from aliyunsdkslb.request.v20140515.CreateLoadBalancerRequest import CreateLoadBalancerRequest
from aliyunsdkslb.request.v20140515.CreateLoadBalancerTCPListenerRequest import CreateLoadBalancerTCPListenerRequest
from aliyunsdkslb.request.v20140515.CreateLoadBalancerUDPListenerRequest import CreateLoadBalancerUDPListenerRequest
from aliyunsdkslb.request.v20140515.CreateMasterSlaveServerGroupRequest import CreateMasterSlaveServerGroupRequest
from aliyunsdkslb.request.v20140515.CreateRulesRequest import CreateRulesRequest
from aliyunsdkslb.request.v20140515.CreateVServerGroupRequest import CreateVServerGroupRequest
from aliyunsdkslb.request.v20140515.DeleteAccessControlListRequest import DeleteAccessControlListRequest
from aliyunsdkslb.request.v20140515.DeleteCACertificateRequest import DeleteCACertificateRequest
from aliyunsdkslb.request.v20140515.DeleteDomainExtensionRequest import DeleteDomainExtensionRequest
from aliyunsdkslb.request.v20140515.DeleteLoadBalancerListenerRequest import DeleteLoadBalancerListenerRequest
from aliyunsdkslb.request.v20140515.DeleteLoadBalancerRequest import DeleteLoadBalancerRequest
from aliyunsdkslb.request.v20140515.DeleteMasterSlaveServerGroupRequest import DeleteMasterSlaveServerGroupRequest
from aliyunsdkslb.request.v20140515.DeleteRulesRequest import DeleteRulesRequest
from aliyunsdkslb.request.v20140515.DeleteServerCertificateRequest import DeleteServerCertificateRequest
from aliyunsdkslb.request.v20140515.DeleteVServerGroupRequest import DeleteVServerGroupRequest
from aliyunsdkslb.request.v20140515.DescribeAccessControlListAttributeRequest import DescribeAccessControlListAttributeRequest
from aliyunsdkslb.request.v20140515.DescribeAccessControlListsRequest import DescribeAccessControlListsRequest
from aliyunsdkslb.request.v20140515.DescribeAvailableResourceRequest import DescribeAvailableResourceRequest
from aliyunsdkslb.request.v20140515.DescribeCACertificatesRequest import DescribeCACertificatesRequest
from aliyunsdkslb.request.v20140515.DescribeDomainExtensionAttributeRequest import DescribeDomainExtensionAttributeRequest
from aliyunsdkslb.request.v20140515.DescribeDomainExtensionsRequest import DescribeDomainExtensionsRequest
from aliyunsdkslb.request.v20140515.DescribeHealthStatusRequest import DescribeHealthStatusRequest
from aliyunsdkslb.request.v20140515.DescribeListenerAccessControlAttributeRequest import DescribeListenerAccessControlAttributeRequest
from aliyunsdkslb.request.v20140515.DescribeLoadBalancerAttributeRequest import DescribeLoadBalancerAttributeRequest
from aliyunsdkslb.request.v20140515.DescribeLoadBalancerHTTPListenerAttributeRequest import DescribeLoadBalancerHTTPListenerAttributeRequest
from aliyunsdkslb.request.v20140515.DescribeLoadBalancerHTTPSListenerAttributeRequest import DescribeLoadBalancerHTTPSListenerAttributeRequest
from aliyunsdkslb.request.v20140515.DescribeLoadBalancerTCPListenerAttributeRequest import DescribeLoadBalancerTCPListenerAttributeRequest
from aliyunsdkslb.request.v20140515.DescribeLoadBalancerUDPListenerAttributeRequest import DescribeLoadBalancerUDPListenerAttributeRequest
from aliyunsdkslb.request.v20140515.DescribeLoadBalancersRequest import DescribeLoadBalancersRequest
from aliyunsdkslb.request.v20140515.DescribeMasterSlaveServerGroupAttributeRequest import DescribeMasterSlaveServerGroupAttributeRequest
from aliyunsdkslb.request.v20140515.DescribeMasterSlaveServerGroupsRequest import DescribeMasterSlaveServerGroupsRequest
from aliyunsdkslb.request.v20140515.DescribeMasterSlaveServerGroupsRequest import DescribeMasterSlaveServerGroupsRequest
from aliyunsdkslb.request.v20140515.DescribeRegionsRequest import DescribeRegionsRequest
from aliyunsdkslb.request.v20140515.DescribeRuleAttributeRequest import DescribeRuleAttributeRequest
from aliyunsdkslb.request.v20140515.DescribeRulesRequest import DescribeRulesRequest
from aliyunsdkslb.request.v20140515.DescribeServerCertificatesRequest import DescribeServerCertificatesRequest
from aliyunsdkslb.request.v20140515.DescribeTagsRequest import DescribeTagsRequest
from aliyunsdkslb.request.v20140515.DescribeVServerGroupAttributeRequest import DescribeVServerGroupAttributeRequest
from aliyunsdkslb.request.v20140515.DescribeVServerGroupsRequest import DescribeVServerGroupsRequest
from aliyunsdkslb.request.v20140515.DescribeZonesRequest import DescribeZonesRequest
from aliyunsdkslb.request.v20140515.ListTagResourcesRequest import ListTagResourcesRequest
from aliyunsdkslb.request.v20140515.ModifyLoadBalancerInstanceSpecRequest import ModifyLoadBalancerInstanceSpecRequest
from aliyunsdkslb.request.v20140515.ModifyLoadBalancerInternetSpecRequest import ModifyLoadBalancerInternetSpecRequest
from aliyunsdkslb.request.v20140515.ModifyLoadBalancerPayTypeRequest import ModifyLoadBalancerPayTypeRequest
from aliyunsdkslb.request.v20140515.ModifyVServerGroupBackendServersRequest import ModifyVServerGroupBackendServersRequest
from aliyunsdkslb.request.v20140515.RemoveAccessControlListEntryRequest import RemoveAccessControlListEntryRequest
from aliyunsdkslb.request.v20140515.RemoveBackendServersRequest import RemoveBackendServersRequest
from aliyunsdkslb.request.v20140515.RemoveListenerWhiteListItemRequest import RemoveListenerWhiteListItemRequest
from aliyunsdkslb.request.v20140515.RemoveTagsRequest import RemoveTagsRequest
from aliyunsdkslb.request.v20140515.RemoveVServerGroupBackendServersRequest import RemoveVServerGroupBackendServersRequest
from aliyunsdkslb.request.v20140515.SetAccessControlListAttributeRequest import SetAccessControlListAttributeRequest
from aliyunsdkslb.request.v20140515.SetBackendServersRequest import SetBackendServersRequest
from aliyunsdkslb.request.v20140515.SetCACertificateNameRequest import SetCACertificateNameRequest
from aliyunsdkslb.request.v20140515.SetDomainExtensionAttributeRequest import SetDomainExtensionAttributeRequest
from aliyunsdkslb.request.v20140515.SetListenerAccessControlStatusRequest import SetListenerAccessControlStatusRequest
from aliyunsdkslb.request.v20140515.SetLoadBalancerDeleteProtectionRequest import SetLoadBalancerDeleteProtectionRequest
from aliyunsdkslb.request.v20140515.SetLoadBalancerHTTPListenerAttributeRequest import SetLoadBalancerHTTPListenerAttributeRequest
from aliyunsdkslb.request.v20140515.SetLoadBalancerHTTPSListenerAttributeRequest import SetLoadBalancerHTTPSListenerAttributeRequest
from aliyunsdkslb.request.v20140515.SetLoadBalancerNameRequest import SetLoadBalancerNameRequest
from aliyunsdkslb.request.v20140515.SetLoadBalancerStatusRequest import SetLoadBalancerStatusRequest
from aliyunsdkslb.request.v20140515.SetLoadBalancerTCPListenerAttributeRequest import SetLoadBalancerTCPListenerAttributeRequest
from aliyunsdkslb.request.v20140515.SetLoadBalancerUDPListenerAttributeRequest import SetLoadBalancerUDPListenerAttributeRequest
from aliyunsdkslb.request.v20140515.SetRuleRequest import SetRuleRequest
from aliyunsdkslb.request.v20140515.SetServerCertificateNameRequest import SetServerCertificateNameRequest
from aliyunsdkslb.request.v20140515.SetVServerGroupAttributeRequest import SetVServerGroupAttributeRequest
from aliyunsdkslb.request.v20140515.StartLoadBalancerListenerRequest import StartLoadBalancerListenerRequest
from aliyunsdkslb.request.v20140515.StopLoadBalancerListenerRequest import StopLoadBalancerListenerRequest
from aliyunsdkslb.request.v20140515.TagResourcesRequest import TagResourcesRequest
from aliyunsdkslb.request.v20140515.UntagResourcesRequest import UntagResourcesRequest
from aliyunsdkslb.request.v20140515.UploadCACertificateRequest import UploadCACertificateRequest
from aliyunsdkslb.request.v20140515.UploadServerCertificateRequest import UploadServerCertificateRequest

@desc_it
def toDescribeLoadBalancersRequest():
    request = DescribeLoadBalancersRequest()
    request.set_LoadBalancerName("扩容")
    oa = request.get_OwnerAccount()
    request.set_accept_format('json')
    return request

@desc_it
def DescRulesRequest(LoadBalancerId="lb-2zejpbwwgitcj5b3aqqst"):
    request = DescribeRulesRequest()
    request.set_LoadBalancerId(LoadBalancerId)
    request.set_ListenerPort(80)
    return request

@desc_it
def DescRuleAttributeRequest(rule_id):
    request = DescribeRuleAttributeRequest()
    request.set_accept_format('json')

    request.set_RuleId(rule_id)
    return request

@desc_it
def DescVServerGroupsRequest(LoadBalancerId):
    request = DescribeVServerGroupsRequest()
    request.set_accept_format('json')
    request.set_LoadBalancerId(LoadBalancerId)
    return request

@desc_it
def DescVServerGroupAttributeRequest(VServerGroupId):
    request = DescribeVServerGroupAttributeRequest()
    request.set_accept_format('json')
    request.set_VServerGroupId(VServerGroupId)
    return request

xs = DescRulesRequest()

vsg_ids = {x['VServerGroupId'] for x in xs['Rules']['Rule']}
print(vsg_ids)
vs_group_attr = DescVServerGroupAttributeRequest(vsg_ids.pop())
print(vs_group_attr)

