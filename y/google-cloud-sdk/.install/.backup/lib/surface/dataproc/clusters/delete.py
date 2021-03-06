# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Delete cluster command."""

from googlecloudsdk.api_lib.dataproc import util
from googlecloudsdk.calliope import base
from googlecloudsdk.calliope import exceptions
from googlecloudsdk.core import log
from googlecloudsdk.core.console import console_io


class Delete(base.Command):
  """Delete a cluster."""

  detailed_help = {
      'DESCRIPTION': '{description}',
      'EXAMPLES': """\
          To delete a cluster, run:

            $ {command} my_cluster
          """,
  }

  @staticmethod
  def Args(parser):
    parser.add_argument('name', help='The name of the cluster to delete.')

  @util.HandleHttpError
  def Run(self, args):
    client = self.context['dataproc_client']
    messages = self.context['dataproc_messages']

    cluster_ref = util.ParseCluster(args.name, self.context)

    request = messages.DataprocProjectsClustersDeleteRequest(
        clusterName=cluster_ref.clusterName,
        projectId=cluster_ref.projectId)

    if not console_io.PromptContinue(
        message="The cluster '{0}' and all attached disks will be "
        'deleted.'.format(args.name)):
      raise exceptions.ToolException('Deletion aborted by user.')

    operation = client.projects_clusters.Delete(request)
    operation = util.WaitForOperation(
        operation, self.context, 'Waiting for cluster deletion operation')
    log.DeletedResource(cluster_ref)

    return operation

  def Display(self, args, result):
    self.format(result)
