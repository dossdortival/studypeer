document.addEventListener('DOMContentLoaded', function () {
  const controls = document.getElementById('membership-controls');
  if (!controls) return;

  const groupId = controls.dataset.groupId;

  controls.addEventListener('click', function (e) {
    if (e.target.id === 'join-btn' || e.target.id === 'leave-btn') {
      const action = e.target.id === 'join-btn' ? 'join' : 'leave';
      fetch(`/groups/${groupId}/${action}/`, {
        method: 'POST',
        headers: {
          'X-CSRFToken': getCookie('csrftoken'),
          'X-Requested-With': 'XMLHttpRequest'
        }
      })
      .then(response => response.json())
      .then(data => {
        if (data.success) {
          updateUI(action);
        } else {
          alert(data.message);
        }
      })
      .catch(error => {
        console.error('Error:', error);
      });
    }
  });

  function updateUI(action) {
    if (action === 'join') {
      controls.innerHTML = `<button id="leave-btn" class="btn btn-danger">Leave Group</button>`;
    } else if (action === 'leave') {
      controls.innerHTML = `<button id="join-btn" class="btn btn-success">Join Group</button>`;
    }

    fetch(window.location.href)
      .then(res => res.text())
      .then(html => {
        const parser = new DOMParser();
        const doc = parser.parseFromString(html, 'text/html');
        const updatedCount = doc.querySelector('#member-count');
        document.getElementById('member-count').innerHTML = updatedCount.innerHTML;
      });
  }

  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let cookie of cookies) {
        cookie = cookie.trim();
        if (cookie.startsWith(name + '=')) {
          cookieValue = decodeURIComponent(cookie.slice(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
});
