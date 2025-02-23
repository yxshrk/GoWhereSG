document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#newactivity').addEventListener('click', compose_activity);


  document.querySelector('form').onsubmit = enter_activity;
  // By default, load the inbox
  defaultview();

  document.querySelectorAll('.addlink').forEach(link => {
    link.onclick=function() {
        const activity_id = this.dataset.postid;

        fetch(`/addtoitinerary/${activity_id}`);

        if (this.innerHTML.trim() === 'Add') {
            this.innerHTML = 'Remove';
        } else {
            this.innerHTML = 'Add';
        }

    };

});

function defaultview() {
  document.querySelector('#create-view').style.display = 'none';
}



function compose_activity() {
  //document.querySelector('#create-view').style.display = 'block';

   if (document.querySelector('#create-view').style.display === 'none') {
    document.querySelector('#create-view').style.display = 'block';
  } else {
    document.querySelector('#create-view').style.display = 'none';
  }

  document.querySelector('#create-title').value = '';
  document.querySelector('#create-content').value = '';
  document.querySelector('#create-category').value = '';
  document.querySelector('#create-cost').value = '';
  document.querySelector('#create-date').value = '';

}

function enter_activity() {

  const title = document.querySelector('#create-title').value;
  const content = document.querySelector('#create-content').value;
  const category = document.querySelector('#create-category').value;
  const cost = document.querySelector('#create-cost').value;
  const date = document.querySelector('#create-date').value;

  fetch('/productivity', {
    method: 'POST',
    body: JSON.stringify({
      title: title,
      content: content,
      category: category,
      cost: cost,
      date: date
    })
  })
  .then(response => response.json())
  .then(result => {
    console.log(result);
  });
  localStorage.clear();

}
});







