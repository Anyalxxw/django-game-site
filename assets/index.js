const questions = document.querySelectorAll('.question')


questions.forEach(question => {
    question.addEventListener('click', () => {
        const li = question.parentElement
        li.classList.toggle('active')
    })
})























