"""Generated message classes for dns version v1.

The Google Cloud DNS API provides services for configuring and serving
authoritative DNS records.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from googlecloudsdk.third_party.apitools.base.protorpclite import messages as _messages


package = 'dns'


class Change(_messages.Message):
  """An atomic update to a collection of ResourceRecordSets.

  Enums:
    StatusValueValuesEnum: Status of the operation (output only).

  Fields:
    additions: Which ResourceRecordSets to add?
    deletions: Which ResourceRecordSets to remove? Must match existing data
      exactly.
    id: Unique identifier for the resource; defined by the server (output
      only).
    kind: Identifies what kind of resource this is. Value: the fixed string
      "dns#change".
    startTime: The time that this operation was started by the server (output
      only). This is in RFC3339 text format.
    status: Status of the operation (output only).
  """

  class StatusValueValuesEnum(_messages.Enum):
    """Status of the operation (output only).

    Values:
      done: <no description>
      pending: <no description>
    """
    done = 0
    pending = 1

  additions = _messages.MessageField('ResourceRecordSet', 1, repeated=True)
  deletions = _messages.MessageField('ResourceRecordSet', 2, repeated=True)
  id = _messages.StringField(3)
  kind = _messages.StringField(4, default=u'dns#change')
  startTime = _messages.StringField(5)
  status = _messages.EnumField('StatusValueValuesEnum', 6)


class ChangesListResponse(_messages.Message):
  """The response to a request to enumerate Changes to a ResourceRecordSets
  collection.

  Fields:
    changes: The requested changes.
    kind: Type of resource.
    nextPageToken: The presence of this field indicates that there exist more
      results following your last page of results in pagination order. To
      fetch them, make another list request using this value as your
      pagination token.  In this way you can retrieve the complete contents of
      even very large collections one page at a time. However, if the contents
      of the collection change between the first and last paginated list
      request, the set of all elements returned will be an inconsistent view
      of the collection. There is no way to retrieve a "snapshot" of
      collections larger than the maximum page size.
  """

  changes = _messages.MessageField('Change', 1, repeated=True)
  kind = _messages.StringField(2, default=u'dns#changesListResponse')
  nextPageToken = _messages.StringField(3)


class DnsChangesCreateRequest(_messages.Message):
  """A DnsChangesCreateRequest object.

  Fields:
    change: A Change resource to be passed as the request body.
    managedZone: Identifies the managed zone addressed by this request. Can be
      the managed zone name or id.
    project: Identifies the project addressed by this request.
  """

  change = _messages.MessageField('Change', 1)
  managedZone = _messages.StringField(2, required=True)
  project = _messages.StringField(3, required=True)


class DnsChangesGetRequest(_messages.Message):
  """A DnsChangesGetRequest object.

  Fields:
    changeId: The identifier of the requested change, from a previous
      ResourceRecordSetsChangeResponse.
    managedZone: Identifies the managed zone addressed by this request. Can be
      the managed zone name or id.
    project: Identifies the project addressed by this request.
  """

  changeId = _messages.StringField(1, required=True)
  managedZone = _messages.StringField(2, required=True)
  project = _messages.StringField(3, required=True)


class DnsChangesListRequest(_messages.Message):
  """A DnsChangesListRequest object.

  Enums:
    SortByValueValuesEnum: Sorting criterion. The only supported value is
      change sequence.

  Fields:
    managedZone: Identifies the managed zone addressed by this request. Can be
      the managed zone name or id.
    maxResults: Optional. Maximum number of results to be returned. If
      unspecified, the server will decide how many results to return.
    pageToken: Optional. A tag returned by a previous list request that was
      truncated. Use this parameter to continue a previous list request.
    project: Identifies the project addressed by this request.
    sortBy: Sorting criterion. The only supported value is change sequence.
    sortOrder: Sorting order direction: 'ascending' or 'descending'.
  """

  class SortByValueValuesEnum(_messages.Enum):
    """Sorting criterion. The only supported value is change sequence.

    Values:
      changeSequence: <no description>
    """
    changeSequence = 0

  managedZone = _messages.StringField(1, required=True)
  maxResults = _messages.IntegerField(2, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(3)
  project = _messages.StringField(4, required=True)
  sortBy = _messages.EnumField('SortByValueValuesEnum', 5, default=u'changeSequence')
  sortOrder = _messages.StringField(6)


class DnsManagedZonesCreateRequest(_messages.Message):
  """A DnsManagedZonesCreateRequest object.

  Fields:
    managedZone: A ManagedZone resource to be passed as the request body.
    project: Identifies the project addressed by this request.
  """

  managedZone = _messages.MessageField('ManagedZone', 1)
  project = _messages.StringField(2, required=True)


class DnsManagedZonesDeleteRequest(_messages.Message):
  """A DnsManagedZonesDeleteRequest object.

  Fields:
    managedZone: Identifies the managed zone addressed by this request. Can be
      the managed zone name or id.
    project: Identifies the project addressed by this request.
  """

  managedZone = _messages.StringField(1, required=True)
  project = _messages.StringField(2, required=True)


class DnsManagedZonesDeleteResponse(_messages.Message):
  """An empty DnsManagedZonesDelete response."""


class DnsManagedZonesGetRequest(_messages.Message):
  """A DnsManagedZonesGetRequest object.

  Fields:
    managedZone: Identifies the managed zone addressed by this request. Can be
      the managed zone name or id.
    project: Identifies the project addressed by this request.
  """

  managedZone = _messages.StringField(1, required=True)
  project = _messages.StringField(2, required=True)


class DnsManagedZonesListRequest(_messages.Message):
  """A DnsManagedZonesListRequest object.

  Fields:
    dnsName: Restricts the list to return only zones with this domain name.
    maxResults: Optional. Maximum number of results to be returned. If
      unspecified, the server will decide how many results to return.
    pageToken: Optional. A tag returned by a previous list request that was
      truncated. Use this parameter to continue a previous list request.
    project: Identifies the project addressed by this request.
  """

  dnsName = _messages.StringField(1)
  maxResults = _messages.IntegerField(2, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(3)
  project = _messages.StringField(4, required=True)


class DnsProjectsGetRequest(_messages.Message):
  """A DnsProjectsGetRequest object.

  Fields:
    project: Identifies the project addressed by this request.
  """

  project = _messages.StringField(1, required=True)


class DnsResourceRecordSetsListRequest(_messages.Message):
  """A DnsResourceRecordSetsListRequest object.

  Fields:
    managedZone: Identifies the managed zone addressed by this request. Can be
      the managed zone name or id.
    maxResults: Optional. Maximum number of results to be returned. If
      unspecified, the server will decide how many results to return.
    name: Restricts the list to return only records with this fully qualified
      domain name.
    pageToken: Optional. A tag returned by a previous list request that was
      truncated. Use this parameter to continue a previous list request.
    project: Identifies the project addressed by this request.
    type: Restricts the list to return only records of this type. If present,
      the "name" parameter must also be present.
  """

  managedZone = _messages.StringField(1, required=True)
  maxResults = _messages.IntegerField(2, variant=_messages.Variant.INT32)
  name = _messages.StringField(3)
  pageToken = _messages.StringField(4)
  project = _messages.StringField(5, required=True)
  type = _messages.StringField(6)


class ManagedZone(_messages.Message):
  """A zone is a subtree of the DNS namespace under one administrative
  responsibility. A ManagedZone is a resource that represents a DNS zone
  hosted by the Cloud DNS service.

  Fields:
    creationTime: The time that this resource was created on the server. This
      is in RFC3339 text format. Output only.
    description: A mutable string of at most 1024 characters associated with
      this resource for the user's convenience. Has no effect on the managed
      zone's function.
    dnsName: The DNS name of this managed zone, for instance "example.com.".
    id: Unique identifier for the resource; defined by the server (output
      only)
    kind: Identifies what kind of resource this is. Value: the fixed string
      "dns#managedZone".
    name: User assigned name for this resource. Must be unique within the
      project. The name must be 1-32 characters long, must begin with a
      letter, end with a letter or digit, and only contain lowercase letters,
      digits or dashes.
    nameServerSet: Optionally specifies the NameServerSet for this
      ManagedZone. A NameServerSet is a set of DNS name servers that all host
      the same ManagedZones. Most users will leave this field unset.
    nameServers: Delegate your managed_zone to these virtual name servers;
      defined by the server (output only)
  """

  creationTime = _messages.StringField(1)
  description = _messages.StringField(2)
  dnsName = _messages.StringField(3)
  id = _messages.IntegerField(4, variant=_messages.Variant.UINT64)
  kind = _messages.StringField(5, default=u'dns#managedZone')
  name = _messages.StringField(6)
  nameServerSet = _messages.StringField(7)
  nameServers = _messages.StringField(8, repeated=True)


class ManagedZonesListResponse(_messages.Message):
  """A ManagedZonesListResponse object.

  Fields:
    kind: Type of resource.
    managedZones: The managed zone resources.
    nextPageToken: The presence of this field indicates that there exist more
      results following your last page of results in pagination order. To
      fetch them, make another list request using this value as your page
      token.  In this way you can retrieve the complete contents of even very
      large collections one page at a time. However, if the contents of the
      collection change between the first and last paginated list request, the
      set of all elements returned will be an inconsistent view of the
      collection. There is no way to retrieve a consistent snapshot of a
      collection larger than the maximum page size.
  """

  kind = _messages.StringField(1, default=u'dns#managedZonesListResponse')
  managedZones = _messages.MessageField('ManagedZone', 2, repeated=True)
  nextPageToken = _messages.StringField(3)


class Project(_messages.Message):
  """A project resource. The project is a top level container for resources
  including Cloud DNS ManagedZones. Projects can be created only in the APIs
  console.

  Fields:
    id: User assigned unique identifier for the resource (output only).
    kind: Identifies what kind of resource this is. Value: the fixed string
      "dns#project".
    number: Unique numeric identifier for the resource; defined by the server
      (output only).
    quota: Quotas assigned to this project (output only).
  """

  id = _messages.StringField(1)
  kind = _messages.StringField(2, default=u'dns#project')
  number = _messages.IntegerField(3, variant=_messages.Variant.UINT64)
  quota = _messages.MessageField('Quota', 4)


class Quota(_messages.Message):
  """Limits associated with a Project.

  Fields:
    kind: Identifies what kind of resource this is. Value: the fixed string
      "dns#quota".
    managedZones: Maximum allowed number of managed zones in the project.
    resourceRecordsPerRrset: Maximum allowed number of ResourceRecords per
      ResourceRecordSet.
    rrsetAdditionsPerChange: Maximum allowed number of ResourceRecordSets to
      add per ChangesCreateRequest.
    rrsetDeletionsPerChange: Maximum allowed number of ResourceRecordSets to
      delete per ChangesCreateRequest.
    rrsetsPerManagedZone: Maximum allowed number of ResourceRecordSets per
      zone in the project.
    totalRrdataSizePerChange: Maximum allowed size for total rrdata in one
      ChangesCreateRequest in bytes.
  """

  kind = _messages.StringField(1, default=u'dns#quota')
  managedZones = _messages.IntegerField(2, variant=_messages.Variant.INT32)
  resourceRecordsPerRrset = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  rrsetAdditionsPerChange = _messages.IntegerField(4, variant=_messages.Variant.INT32)
  rrsetDeletionsPerChange = _messages.IntegerField(5, variant=_messages.Variant.INT32)
  rrsetsPerManagedZone = _messages.IntegerField(6, variant=_messages.Variant.INT32)
  totalRrdataSizePerChange = _messages.IntegerField(7, variant=_messages.Variant.INT32)


class ResourceRecordSet(_messages.Message):
  """A unit of data that will be returned by the DNS servers.

  Fields:
    kind: Identifies what kind of resource this is. Value: the fixed string
      "dns#resourceRecordSet".
    name: For example, www.example.com.
    rrdatas: As defined in RFC 1035 (section 5) and RFC 1034 (section 3.6.1).
    ttl: Number of seconds that this ResourceRecordSet can be cached by
      resolvers.
    type: The identifier of a supported record type, for example, A, AAAA, MX,
      TXT, and so on.
  """

  kind = _messages.StringField(1, default=u'dns#resourceRecordSet')
  name = _messages.StringField(2)
  rrdatas = _messages.StringField(3, repeated=True)
  ttl = _messages.IntegerField(4, variant=_messages.Variant.INT32)
  type = _messages.StringField(5)


class ResourceRecordSetsListResponse(_messages.Message):
  """A ResourceRecordSetsListResponse object.

  Fields:
    kind: Type of resource.
    nextPageToken: The presence of this field indicates that there exist more
      results following your last page of results in pagination order. To
      fetch them, make another list request using this value as your
      pagination token.  In this way you can retrieve the complete contents of
      even very large collections one page at a time. However, if the contents
      of the collection change between the first and last paginated list
      request, the set of all elements returned will be an inconsistent view
      of the collection. There is no way to retrieve a consistent snapshot of
      a collection larger than the maximum page size.
    rrsets: The resource record set resources.
  """

  kind = _messages.StringField(1, default=u'dns#resourceRecordSetsListResponse')
  nextPageToken = _messages.StringField(2)
  rrsets = _messages.MessageField('ResourceRecordSet', 3, repeated=True)


class StandardQueryParameters(_messages.Message):
  """Query parameters accepted by all methods.

  Enums:
    AltValueValuesEnum: Data format for the response.

  Fields:
    alt: Data format for the response.
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters. Overrides userIp if both are provided.
    trace: A tracing token of the form "token:<tokenid>" to include in api
      requests.
    userIp: IP address of the site where the request originates. Use this if
      you want to enforce per-user limits.
  """

  class AltValueValuesEnum(_messages.Enum):
    """Data format for the response.

    Values:
      json: Responses with Content-Type of application/json
    """
    json = 0

  alt = _messages.EnumField('AltValueValuesEnum', 1, default=u'json')
  fields = _messages.StringField(2)
  key = _messages.StringField(3)
  oauth_token = _messages.StringField(4)
  prettyPrint = _messages.BooleanField(5, default=True)
  quotaUser = _messages.StringField(6)
  trace = _messages.StringField(7)
  userIp = _messages.StringField(8)


