if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone Jkdeveloper01/TOM-BOT.git /TOM-BOT
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /TOM-BOT
fi
cd /TOM-BOT
pip3 install -U -r requirements.txt
echo "Starting...."
python3 bot.py
