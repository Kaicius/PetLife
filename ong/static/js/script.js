const tabButtons = document.querySelectorAll('.tab-button');
  tabButtons.forEach(button => {
    button.addEventListener('click', () => {
      tabButtons.forEach(btn => btn.classList.remove('active'));
      button.classList.add('active');
    });
  });

document.querySelectorAll('.pet-card').forEach(card => {
    card.addEventListener('click', () => {
      const modal = new bootstrap.Modal(document.getElementById('adocaoModal'));
      modal.show();
    });
  });