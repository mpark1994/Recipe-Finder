function comment(element, post_id) {
    fetch(`/recipe-comment/${post_id}`)
    .then(() => {
        location.reload()
    })
}

function favorite(element, post_id) {
    fetch(`/recipe-favorite/${post_id}`)
    .then(() => {
        location.reload()
    })
}

// function subscribe(element, id) {
//     console.log(id)
//     fetch(`/subscribe/${id}`)
//     .then(() => {
//         location.reload()
//     })
// }
