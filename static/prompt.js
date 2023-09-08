const promptForm = document.getElementById("prompt-form");
const submitButton = document.getElementById("submit-button");
const questionButton = document.getElementById("question-button");
const qcmButton = document.getElementById("qcm-button");
const messagesContainer = document.getElementById("messages-container");
const DarkButton = document.getElementById("Dark-Mode");

const appendHumanMessage = (message) => {
  const humanMessageElement = document.createElement("div");
  humanMessageElement.classList.add("message", "message-human");
  humanMessageElement.innerHTML = message;
  messagesContainer.appendChild(humanMessageElement);
};

const appendAIMessage = async (messagePromise) => {
  // Add a loader to the interface
  const loaderElement = document.createElement("div");
  loaderElement.classList.add("message");
  loaderElement.innerHTML =
    "<div class='loader'><div></div><div></div><div></div>";
  messagesContainer.appendChild(loaderElement);

  // Await the answer from the server
  const messageToAppend = await messagePromise();

  // Replace the loader with the answer
  loaderElement.classList.remove("loader");
  loaderElement.innerHTML = messageToAppend;
};

const handlePrompt = async (event) => {
  event.preventDefault();
  // Parse form data in a structured object
  const data = new FormData(event.target);
  promptForm.reset();

  let url = "/prompt";
  if (questionButton.dataset.question !== undefined) {
    url = "/answer";
    data.append("question", questionButton.dataset.question);
    delete questionButton.dataset.question;
    questionButton.classList.remove("hidden");
    qcmButton.classList.remove("hidden");
    submitButton.innerHTML = "Message";
  }
  if (qcmButton.dataset.qcm !== undefined) {
    url = "/answerQCM";
    data.append("qcm", qcmButton.dataset.qcm);
    delete qcmButton.dataset.qcm;
    qcmButton.classList.remove("hidden");
    questionButton.classList.remove("hidden");
    submitButton.innerHTML = "Message";
  }


  appendHumanMessage(data.get("prompt"));

  await appendAIMessage(async () => {
    const response = await fetch(url, {
      method: "POST",
      body: data,
    });
    const result = await response.json();
    return result.answer;
  });
};

promptForm.addEventListener("submit", handlePrompt);

const handleQuestionClick = async (event) => {
  appendAIMessage(async () => {
    const response = await fetch("/question", {
      method: "GET",
    });
    const result = await response.json();
    const question = result.answer;

    questionButton.dataset.question = question;
    questionButton.classList.add("hidden");
    qcmButton.classList.add("hidden")
    submitButton.innerHTML = "Répondre à la question";
    return question;
  });
};

questionButton.addEventListener("click", handleQuestionClick);

const handleQcmClick = async (event) => {
  appendAIMessage(async () => {
    const response = await fetch("/qcm", {
      method: "GET",
    });
    const result = await response.json();
    const qcm = result.answer;

    questionButton.classList.add("hidden");
    qcmButton.classList.add("hidden")
    submitButton.innerHTML = "Réponse";

    qcmButton.dataset.qcm = qcm;
    return qcm;
  });
};

qcmButton.addEventListener("click", handleQcmClick);
/*
function activerDarkMode() {
  const root = document.documentElement;
  root.style.setProperty('--main-background-color', 'black');
  root.style.setProperty('--main-color', 'white');
  root.style.setProperty('--secondary-color', '#3f3d3d');
  root.style.setProperty('--border-color', 'white');
  root.style.setProperty('--body-background-color', '#3f3d3d')


  
  human.style.setProperty('background-color', '#3f3d3d');


}





DarkButton.addEventListener("click", () => {
  activerDarkMode();
});  */


const root = document.documentElement;


// Fonction pour activer le mode sombre
function activerDarkMode() {
  root.style.setProperty('--main-background-color', 'black');
  root.style.setProperty('--main-color', 'white');
  root.style.setProperty('--secondary-color', '#3f3d3d');
  root.style.setProperty('--border-color', 'white');
  root.style.setProperty('--body-background-color', '#3f3d3d')







}
// Fonction pour désactiver le mode sombre
function desactiverDarkMode() {
  // Mettez ici le code pour désactiver le mode sombre (revenir au mode clair)
  root.style.setProperty('--main-color', '#2a303b');
  root.style.setProperty('--secondary-color', '#dfe374');
  root.style.setProperty('--border-color', '#ef0b0b');
  root.style.setProperty('--body-background-color', '#f8f6f5')
  root.style.setProperty('--main-background-color', '##ffffff')







}

// Ajoutez un gestionnaire d'événements "click" au bouton de bascule du mode sombre
DarkButton.addEventListener("click", () => {
  // Vérifiez si le mode sombre est actuellement activé

  const bodyBackgroundColor = getComputedStyle(document.body).getPropertyValue("--main-background-color");
  const modeSombreActive = bodyBackgroundColor === "black";
  // Si le mode sombre est activé, désactivez-le ; sinon, activez-le
  console.log()
  if (modeSombreActive) {
    desactiverDarkMode();
  } else {
    activerDarkMode();
  }
}
)
  ;







