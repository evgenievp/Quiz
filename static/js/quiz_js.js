function timer() {

    async function hideQuestions() {
        let elStorage = [];
        for (let i = 1; i < 6; i++) {
            let questionEl = document.getElementById(`question-number${i}`);
            elStorage.push(questionEl);
            questionEl.remove();
        }

        let jsContainer = document.getElementById('js_container');
        let displayTimer = document.createElement("h1");
        jsContainer.appendChild(displayTimer);
        // main for loop. //
        for (let i = 1; i < 6; i++) {
            let el = elStorage.shift();
            jsContainer.appendChild(el);
            let time = 5;
            while (time > 0) {
                time -= 1;
                displayTimer.textContent = time;
                await delay(1000);
            }

            function delay(ms) {
                return new Promise(resolve => setTimeout(resolve, ms));
            }

            jsContainer.removeChild(el);

            // await until next question. //
            time = 3;
            while (time > 0) {
                time -= 1;
                displayTimer.textContent = `Time until next question: ${time}`;
                await delay(1000);
            }

            if (i === 5) {
                break;
            }
        }


    }

    hideQuestions();
}

function buttons() {
    let correctAnswer = document.getElementById("valid-option");
    let text = correctAnswer.textContent;
    let button = document.getElementsByClassName(`${text}`);
    let correctButton = button[0];
    correctButton.style.backgroundColor = "lightgreen";

}
