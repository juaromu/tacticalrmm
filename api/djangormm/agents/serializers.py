from rest_framework import serializers

from .models import Agent

class AgentSerializer(serializers.ModelSerializer):

    patches_pending = serializers.ReadOnlyField(source="has_patches_pending")
    
    class Meta:
        model = Agent
        fields = (
            "id",
            "version",
            "operating_system",
            "plat",
            "plat_release",
            "hostname",
            "local_ip",
            "agent_id",
            "last_seen",
            "services",
            "public_ip",
            "cpu_load",
            "total_ram",
            "used_ram",
            "disks",
            "boot_time",
            "logged_in_username",
            "cpu_info",
            "client",
            "antivirus",
            "site",
            "monitoring_type",
            "description",
            "mesh_node_id",
            "overdue_email_alert",
            "overdue_text_alert",
            "overdue_time",
            "status",
            "uninstall_pending",
            "uninstall_inprogress",
            "ping_check_interval",
            "patches_pending",
        )

class AgentHostnameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ("hostname",)