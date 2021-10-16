
let searchable = [
  'Dodoma','Arusha',
  'Mwanza','Dar es Salaam',
  'Geita','Iringa',
  'Kagera','Kigoma',
  'Katavi','Kilimanjaro',
  'Lindi', 'Manyara',
  'Mara', 'Mara', 'Mbeya',
  'Zanzibar', 'Morogoro',
  'Mtwara', 'Njombe', 'Pwani',
  'Rukwa', 'Ruvuma',
  'Shinyanga', 'Simiyu',
  'Singida', 'Tabora', 'Tanga',
];

const searchInput = document.getElementById('search');
const searchWrapper = document.querySelector('.wrapper');
const resultsWrapper = document.querySelector('.results');

searchInput.addEventListener('keyup', () => {
  let results = [];
  let input = searchInput.value;
  if (input.length) {
    results = searchable.filter((item) => {
      return item.toLowerCase().includes(input.toLowerCase());
    });
  }
  renderResults(results);
});

function renderResults(results) {
  if (!results.length) {
    return searchWrapper.classList.remove('show');
  }

  const content = results
    .map((item) => {
//      return `<li>${item}</li>`;
return `<div class="country filter-control hide"><form action="" method="post" class="contact-form">

                        <input type="hidden" name="region" value="${item}">
                        <input type="submit" value="${item}" placeholder="Send message">
                    </form>
                </div>`;
    })

    .join('');

  searchWrapper.classList.add('show');
  resultsWrapper.innerHTML = `<div>${content}</div>`;
}
