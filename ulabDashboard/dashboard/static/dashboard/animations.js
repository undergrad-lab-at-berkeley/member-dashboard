console.log('hey');

$('.profile-arrow').on('click', function() {
  $('.profile-menu').toggleClass('show');
});

$('body').on('mouseup', function(e) {
  if (!$('.profile-menu').is(e.target) && !$('.profile-arrow').is(e.target) &&
    $('.profile-menu').has(e.target).length === 0) {
      $('.profile-menu').removeClass('show');
  }
});