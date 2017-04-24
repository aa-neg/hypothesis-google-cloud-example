while [[ $# -gt 1  ]]
do
  key="$1"

case $key in
    -fn|--fileName)
    FILENAME="$2"
    shift
    ;;
     -bn|--bucketName)
    BUCKETNAME="$2"
    shift 
    ;;
    -bp|--basePath)
    BASEPATH="$2"
    shift
    ;;
    *)
    ;;
esac
shift
done

echo 'Uploading file from downloads to google cloud storage.'
read -n 1 -s -p "Press any key to continue"
printf '\n\n'
gsutil cp ${BASEPATH}${FILENAME} gs://${BUCKETNAME}/${FILENAME}

printf '\n\n'
echo 'About to run script...'
read -n 1 -s -p "Press any key to continue"
printf '\n\n'

exec python3 detect_landmark.py gs://${BUCKETNAME}/${FILENAME}
