mkdir app/static/
for card in $(cat dominion_data/card_list); 
do wget https://wiki.dominionstrategy.com/images/${card}Digital.jpg -P app/static/img; 
done;


wget -r -np -nH -A  'Digital.jpg' http://wiki.dominionstrategy.com/images/