# Copyright 2014 Google Inc. All Rights Reserved.
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

"""The main command group for cloud container."""

import argparse
import os
from googlecloudsdk.api_lib.container import api_adapter
from googlecloudsdk.calliope import actions
from googlecloudsdk.calliope import base
from googlecloudsdk.core import properties


@base.ReleaseTracks(base.ReleaseTrack.GA)
class Container(base.Group):
  """Deploy and manage clusters of machines for running containers."""

  DEFAULT_API_VERSION = 'v1'

  @staticmethod
  def Args(parser):
    """Add arguments to the parser.

    Args:
      parser: argparse.ArgumentParser, This is a standard argparser parser with
        which you can register arguments.  See the public argparse documentation
        for its capabilities.
    """
    parser.add_argument(
        '--api-version', help=argparse.SUPPRESS,
        action=actions.StoreProperty(
            properties.VALUES.api_client_overrides.container))
    parser.add_argument(
        '--zone', '-z',
        help='The compute zone (e.g. us-central1-a) for the cluster',
        action=actions.StoreProperty(properties.VALUES.compute.zone))

  def Filter(self, context, args):
    """Modify the context that will be given to this group's commands when run.

    Args:
      context: {str:object}, A set of key-value pairs that can be used for
          common initialization among commands.
      args: argparse.Namespace: The same namespace given to the corresponding
          .Run() invocation.

    Returns:
      The refined command context.
    """
    api_version = (properties.VALUES.api_client_overrides.container.Get()
                   or self.DEFAULT_API_VERSION)
    endpoint_url = properties.VALUES.api_endpoint_overrides.container.Get()
    comp_endpoint_url = properties.VALUES.api_endpoint_overrides.compute.Get()
    context['api_adapter'] = api_adapter.NewAPIAdapter(
        api_version, endpoint_url, comp_endpoint_url, self.Http())
    return context


@base.ReleaseTracks(base.ReleaseTrack.BETA)
class ContainerBeta(Container):
  """Deploy and manage clusters of machines for running containers."""


@base.ReleaseTracks(base.ReleaseTrack.ALPHA)
class ContainerAlpha(Container):
  """Deploy and manage clusters of machines for running containers."""


