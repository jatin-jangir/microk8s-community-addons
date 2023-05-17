import pytest
import os
import platform

from utils import (
    microk8s_disable,
    microk8s_enable,
    wait_for_pod_state,
)


class TestDevtron(object):
    @pytest.mark.skipif(
        platform.machine() != "x86_64",
        reason="Devtron tests are only relevant in x86 architectures",
    )
    @pytest.mark.skipif(
        os.environ.get("UNDER_TIME_PRESSURE") == "True",
        reason="Skipping devtron tests as we are under time pressure",
    )
    def test_devtron(self):
        """
        Sets up and validates Devtron.
        """
        print("Enabling devtron")
        microk8s_enable("devtron")
        print("Validating devtron")
        self.validate_devtron()
        print("Disabling devtron")
        microk8s_disable("devtron")

    def validate_devtron(self):
        """
        Validate devtron
        """
        wait_for_pod_state(
            "", "devtroncd", "running", label="release=devtron"
        )
