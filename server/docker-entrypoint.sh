#!/bin/bash

echo ""
echo ""

APP="/app/app.py"           
CONFIG="/app/settings.py" 

# Validate parameters
if [ -z "$SLACK_TOKEN" ]; then
    echo "Missing: Slack token. Use '-e SLACK_TOKEN=<slack_token>'"
    exit 1
fi
if [ -z "$SLACK_CHANNEL" ]; then
    echo "Missing: Slack channel. Use '-e SLACK_CHANNEL=<slack_channel>'"
    exit 1
fi
if [ -z "$SLACK_ICON_URL" ]; then
    echo "Missing: Slack icon url. Use '-e SLACK_ICON_URL=<slack_icon_url>'"
    exit 1
fi
if [ -z "$SLACK_USER_NAME" ]; then
    echo "Missing: Slack channel. Use '-e SLACK_USER_NAME=<slack_user_name>'"
    exit 1
fi


echo "Slack token: $SLACK_TOKEN"
echo "Slack channel: $SLACK_CHANNEL"
echo "Slack icon url: $SLACK_ICON_URL"
echo "Slack user name: $SLACK_USER_NAME"
echo ""

# Copy sample settings
cp -f "/app/settings_sample.py" $CONFIG

# Update settings
sed -i "s/<slack_token>/$SLACK_TOKEN/" $CONFIG
sed -i "s/<slack_channel>/$SLACK_CHANNEL/" $CONFIG
sed -i "s,<slack_icon_url>,$SLACK_ICON_URL," $CONFIG
sed -i "s/<slack_user_name>/$SLACK_USER_NAME/" $CONFIG

# Hand off to the CMD
exec "$@"
