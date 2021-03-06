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
"""Describe cluster command."""
from googlecloudsdk.calliope import base
from googlecloudsdk.core import log
from surface.container.clusters.upgrade import UpgradeHelpText
from surface.container.clusters.upgrade import VersionVerifier
from googlecloudsdk.third_party.py27 import py27_collections as collections


class Describe(base.Command):
  """Describe an existing cluster for running containers."""

  @staticmethod
  def Args(parser):
    """Register flags for this command.

    Args:
      parser: An argparse.ArgumentParser-like object. It is mocked out in order
          to capture some information, but behaves like an ArgumentParser.
    """
    parser.add_argument('name', help='The name of this cluster.')

  def Run(self, args):
    """This is what gets called when the user runs this command.

    Args:
      args: an argparse namespace. All the arguments that were provided to this
        command invocation.

    Returns:
      Some value that we want to have printed later.
    """
    adapter = self.context['api_adapter']
    describe_info = collections.namedtuple('describe_info', ['cluster', 'text'])
    text = None
    vv = VersionVerifier()
    c = adapter.GetCluster(adapter.ParseCluster(args.name))
    ver_status = vv.Compare(c.currentMasterVersion, c.currentNodeVersion)
    if ver_status == VersionVerifier.UPGRADE_AVAILABLE:
      text = UpgradeHelpText.UPGRADE_AVAILABLE
    elif ver_status == VersionVerifier.SUPPORT_ENDING:
      text = UpgradeHelpText.SUPPORT_ENDING
    elif ver_status == VersionVerifier.UNSUPPORTED:
      text = UpgradeHelpText.UNSUPPORTED
    if ver_status != VersionVerifier.UP_TO_DATE:
      text += UpgradeHelpText.UPGRADE_COMMAND.format(name=c.name)
    return describe_info(c, text)

  def Display(self, args, result):
    """This method is called to print the result of the Run() method.

    Args:
      args: The arguments that command was run with.
      result: The value returned from the Run() method.
    """
    self.format(result.cluster)
    if result.text:
      log.status.Print(result.text)
