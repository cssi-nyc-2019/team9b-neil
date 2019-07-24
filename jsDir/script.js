let questions = [
	{q: "What is the largest continent?", img: "https://cdn.pixabay.com/photo/2016/04/24/04/53/globe-1348777_960_720.png", ans1: "Asia"},
	{q: "What is the tallest mammal?", img: "https://cdn130.picsart.com/272398031031211.png?r1024x1024", ans2: "Giraffe"},
	{q: "What is the capital of Italy?", img: "https://www.worldatlas.com/webimage/countrys/namerica/usstates/newgraphics/major.gif", ans3: "Rome"},
	{q: "How many sides does a hexagon have?", img: "https://ds055uzetaobb.cloudfront.net/brioche/solvable/cdc4c56e6b.85e98b9fb0.SIjhyT.png?width=250", ans4: "6"},
	{q: "What is the full name of Michael Jackson?", img: "https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Michael_Jackson_signature.svg/1200px-Michael_Jackson_signature.svg.png", ans5: "Michael Joseph Jackson"},
	{q: "Who is the creator of Facebook?", img: "https://i.pinimg.com/originals/41/28/2b/41282b58cf85ddaf5d28df96ed91de98.png", ans6: "Mark Zuckerberg"},
	{q: "When was Google founded?", img: "https://learnlaunch.org/wp-content/uploads/2016/11/google-logo.png", ans7: "1998"},
	{q: "Which ocean is the deepest?", img: "https://oceanservice.noaa.gov/ocean/ocean.png", ans8: "Pacific Ocean"},
	{q: "Where was Obama born?", img: "https://i.pinimg.com/originals/df/75/74/df7574157e8c97891c7ac7eae24629ac.png", ans10: "Hawaii"},
	{q: "Which planet is closest to the sun?", img: "https://cdn2.iconfinder.com/data/icons/business-areas-1/512/solar_system-512.png", ans11: "Mercury"},
	{q: "Whose picture is on a dime?", img: "http://www.pngmart.com/files/3/American-Silver-Coin-Transparent-PNG.png", ans12:"Franklin D. Roosevelt"},
    {q: "Who is the richest person in the world", img: "https://stijndewitt.files.wordpress.com/2018/04/money1.png?w=723", ans13: "Jeff Bezos"},
    {q: "How do you say goodbye in Japanese?", img: "https://www.gulfcoast.edu/images/language-literature/goodbye.png", ans14: "Sayonara"},
    {q: "How many strings  does a cello have?", img: "https://cdn.shopify.com/s/files/1/2966/4646/products/120_Cello_-_Full_-_Front-800x800_1_4000x.png?v=1538070559", ans15: "4"},
    {q: "What is the currency in Japan?", img: "", ans16: "Yen"},
];

// let possibleAnswers = [
//     {a1: "North America", a2: "Africa"}
// ]

function displayQuestion(){
        // <label>
        //     <input name="${i}" type="radio" class="correct"></input>
        //     <img width="210px" height="200px" src= "${questions[i].image}">
        // </label>
    for (i = 0; i < questions.length; i++){
    	console.log(questions[i]);
    }
}
displayQuestion();