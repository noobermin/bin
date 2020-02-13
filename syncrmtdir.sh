syncdir(){
    CMD=$1
    ADDR=$HOMEUSER@$HOMEHOST
    DIR=$(sed 's/\/$//' <<<$2)
    ARGS=$([ "$CMD" == "up" ] &&
	       echo $DIR ${ADDR}:$(dirname $DIR)/ ||
		   echo ${ADDR}:$DIR $(dirname $DIR)/ )
    [ -n "$N" ] && N=-n
    if [ -n "$DRYRUN" ]; then
	echo rsync --rsh="ssh $HOMESSHOPTS" -aPru $N --delete $ARGS
	return 
    fi
    rsync --rsh="ssh $HOMESSHOPTS" -aPru $N --delete $ARGS
}

