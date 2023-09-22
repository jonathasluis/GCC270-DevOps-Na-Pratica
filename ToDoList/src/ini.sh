diretorio="migrations"

if [ -d "$diretorio" ]; then
    echo "O diretório $diretorio existe."
else
    flask db init
fi

flask db init
flask db migrate
flask db upgrade
python app.py