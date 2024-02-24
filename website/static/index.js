function deleteNote(nodeId) {
  fetch('/delete-note', {
    method: 'POST',
    body: JSON.stringify({nodeId: nodeId}),
  }).then((_res) => {
    window.location.href = "/";
  });

}
