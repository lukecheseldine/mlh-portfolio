const timelineForm = document.getElementById('timeline-form');
const timeline = document.getElementById('timeline');

timelineForm.addEventListener('submit', (e) => {
    e.preventDefault();

    const payload = new FormData(timelineForm);
    
    fetch('/api/timeline_post', {
        method: 'POST',
        body: payload,
    })
    .then(res => res.json())
    .then(data => console.log(data))
    
    fetch('/api/timeline_post', {
        method: 'GET',
    })
    .then(res => res.json())
    .then(data => updateDisplay(data))

})

function updateDisplay(data) {
    timeline.innerHTML = '';
    console.log(data['timeline_posts'].reverse())
    data['timeline_posts'].reverse().forEach((postData) => {

        // wrapper
        post = document.createElement('div');
        post.classList.add('post');
        post.setAttribute('data-post-id', postData['id'])

        // content
        const name = document.createElement('div');
        name.classList.add('name');
        const nameLabel = document.createElement('p')
        nameLabel.classList.add('name-label')
        nameLabel.innerText = 'Author'
        const nameContent = document.createElement('p')
        nameContent.classList.add('name-content')
        nameContent.innerText = postData['name'];
        name.appendChild(nameLabel)
        name.appendChild(nameContent)

        const email = document.createElement('div');
        email.classList.add('email');
        const emailLabel = document.createElement('p')
        emailLabel.classList.add('email-label')
        emailLabel.innerText = 'Email'
        const emailContent = document.createElement('p')
        emailContent.classList.add('email-content')
        emailContent.innerText = postData['email'];
        email.appendChild(emailLabel)
        email.appendChild(emailContent)

        const content = document.createElement('div');
        content.classList.add('content');
        const contentLabel = document.createElement('p')
        contentLabel.classList.add('content-label')
        contentLabel.innerText = 'Content'
        const contentContent = document.createElement('p')
        contentContent.classList.add('content-content')
        contentContent.innerText = postData['content'];
        content.appendChild(contentLabel)
        content.appendChild(contentContent)

        const date = document.createElement('div');
        date.classList.add('date');
        const dateLabel = document.createElement('p')
        dateLabel.classList.add('date-label')
        dateLabel.innerText = 'Date'
        const dateContent = document.createElement('p')
        dateContent.classList.add('date-content')
        dateContent.innerText = postData['created_at'];
        date.appendChild(dateLabel)
        date.appendChild(dateContent)

        // put together
        post.appendChild(name)
        post.appendChild(email)
        post.appendChild(date)
        post.appendChild(content)
        timeline.appendChild(post)
    })
}

fetch('/api/timeline_post', {
    method: 'GET',
})
.then(res => res.json())
.then(data => updateDisplay(data))