// =====================================
//      CLOSE HELPERS
// =====================================

function closeResult(){
    document.getElementById("resultContent").innerHTML =
        "<h2>Word Information</h2><p>Search a word to begin.</p>";
    document.querySelector("#result .close-btn").style.display = "none";
}

function closeGameArea(){
    document.getElementById("gameContent").innerHTML = "";
    document.querySelector("#gameArea .close-btn").style.display = "none";
}

// =====================================
//      DISPLAY WORD
// =====================================

function showWord(word){

    let html = `
        <h2>${word.name}</h2>
        <p><b>Category:</b> ${word.category}</p>
        <p><b>Meaning:</b><br>${word.meaning}</p>
    `;

    document.getElementById("resultContent").innerHTML = html;
    document.querySelector("#result .close-btn").style.display = "inline-block";
}

// =====================================
// SEARCH WORD
// =====================================

function searchWord(){

    let word = document.getElementById("searchInput").value;

    fetch("/search?word=" + encodeURIComponent(word))
    .then(response=>response.json())
    .then(data=>{

        if(data.error){
            document.getElementById("resultContent").innerHTML = "<h2>Word Not Found</h2>";
            document.querySelector("#result .close-btn").style.display = "inline-block";
        } else {
            showWord(data);
        }

    });

}

// =====================================
// BROWSE DICTIONARY
// =====================================

function browseWords(){

    fetch("/browse")
    .then(response=>response.json())
    .then(words=>{

        let html="<h2>Dictionary</h2>";

        words.forEach(word=>{
            html+=`
            <div class="word">
                <h3>${word.name}</h3>
                <p><b>${word.category}</b></p>
                <p>${word.meaning}</p>
            </div>
            `;
        });

        document.getElementById("resultContent").innerHTML = html;
        document.querySelector("#result .close-btn").style.display = "inline-block";

    });

}

// =====================================
// RANDOM WORD
// =====================================

function randomWord(){
    fetch("/random")
    .then(response=>response.json())
    .then(word=>{ showWord(word); });
}

// =====================================
// WORD OF THE DAY
// =====================================

function wordOfDay(){
    fetch("/wordofday")
    .then(response=>response.json())
    .then(word=>{ showWord(word); });
}

// =====================================
// FLASHCARD
// =====================================

function flashcards(){

    fetch("/random")
    .then(response=>response.json())
    .then(word=>{

        let html=`
        <h2>Flashcard</h2>
        <div class="card">
            <h3>${word.name}</h3>
            <button onclick="alert('${word.meaning}')">Reveal Meaning</button>
        </div>
        <br>
        <button onclick="flashcards()">Next Card →</button>
        `;

        document.getElementById("gameContent").innerHTML = html;
        document.querySelector("#gameArea .close-btn").style.display = "inline-block";

    });

}

// =====================================
// GUESS THE WORD
// =====================================

// =====================================
// GUESS THE WORD
// =====================================

let currentGuessWord = null;

function guessWord(){

    fetch("/random")
    .then(response=>response.json())
    .then(word=>{

        currentGuessWord = word;

        let html=`
        <h2>Guess the Word</h2>
        <p>${word.meaning}</p>

        <input type="text" id="guessInput" placeholder="Enter your answer">
        <button onclick="checkGuess()">Submit</button>

        <p id="guessResult"></p>
        `;

        document.getElementById("gameContent").innerHTML = html;
        document.querySelector("#gameArea .close-btn").style.display = "inline-block";

    });

}

function checkGuess(){

    let answer = document.getElementById("guessInput").value;

    if(answer.toLowerCase() === currentGuessWord.name.toLowerCase()){
        document.getElementById("guessResult").innerHTML =
            "<b style='color:green;'>Correct!</b>";
    } else {
        document.getElementById("guessResult").innerHTML =
            "<b style='color:red;'>Wrong! Correct Answer: "+currentGuessWord.name+"</b>";
    }

    document.getElementById("guessResult").innerHTML +=
        `<br><br><button onclick="guessWord()">Next Word →</button>`;

}

// =====================================
// MCQ QUIZ
// =====================================

function mcqQuiz(){

    fetch("/browse")
    .then(response=>response.json())
    .then(words=>{

        let question = words[Math.floor(Math.random()*words.length)];
        let options=[question.name];

        while(options.length<4){
            let random = words[Math.floor(Math.random()*words.length)].name;
            if(!options.includes(random)) options.push(random);
        }

        options.sort(()=>Math.random()-0.5);

        let html=`
        <h2>MCQ Quiz</h2>
        <p>${question.meaning}</p>
        `;

        options.forEach(option=>{
            html+=`
            <button onclick="checkAnswer('${option}','${question.name}')">${option}</button>
            <br><br>
            `;
        });

        html += `<div id="nextBtnWrap"></div>`;

        document.getElementById("gameContent").innerHTML = html;
        document.querySelector("#gameArea .close-btn").style.display = "inline-block";

    });

}

// =====================================
// CHECK ANSWER
// =====================================

function checkAnswer(selected,correct){

    if(selected===correct){
        alert("Correct!");
    } else {
        alert("Wrong!\nCorrect Answer: "+correct);
    }

    document.getElementById("nextBtnWrap").innerHTML =
        `<button onclick="mcqQuiz()">Next Question →</button>`;

}