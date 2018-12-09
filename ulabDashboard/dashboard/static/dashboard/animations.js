console.log('hey');
// $('.profile-menu').toggleClass('show');
$('<br />').insertBefore('#id_memberForm-about');
$('<br />').insertBefore('#id_announcementForm-description');


$('.profile-menu-btn').on('click', function() {
  $('.profile-menu').toggleClass('show');
  $('.profile-arrow').toggleClass('is-active');
});

$('body').on('mouseup', function(e) {
  if (!$('.profile-menu-btn').is(e.target) && !$('.profile-arrow').is(e.target) &&
    $('.profile-menu').has(e.target).length === 0) {
      $('.profile-menu').removeClass('show');
      $('.profile-arrow').removeClass('is-active');
  }
});

$('.click-overlay').on('click', function() {
  $('.click-overlay').removeClass('show');
  $('.login-container').removeClass('show');
});

$('.show-login-btn').on('click', function() {
  $('.profile-menu').removeClass('show');
  $('.click-overlay').addClass('show');
  $('.login-container').addClass('show');
});

$('.login-forgot').on('click', function() {
  alert('lol good luck kid');
});