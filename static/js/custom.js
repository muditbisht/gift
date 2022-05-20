
	//---------menu------------//

		/*global $ */
		

			"use strict";

			$('.menu > ul > li:has( > ul)').addClass('menu-dropdown-icon');
			//Checks if li has sub (ul) and adds class for toggle icon - just an UI


			$('.menu > ul > li > ul:not(:has(ul))').addClass('normal-sub');
			//Checks if drodown menu's li elements have anothere level (ul), if not the dropdown is shown as regular dropdown, not a mega menu (thanks Luka Kladaric)

			$(".menu > ul").before("<a href=\"#\" class=\"menu-mobile\"></a>");

			//Adds menu-mobile class (for mobile toggle menu) before the normal menu
			//Mobile menu is hidden if width is more then 959px, but normal menu is displayed
			//Normal menu is hidden if width is below 959px, and jquery adds mobile menu
			//Done this way so it can be used with wordpress without any trouble

			$(".menu > ul > li").hover(function (e) {
				if ($(window).width() > 943) {
					$(this).children("ul").stop(true, false).slideToggle(350);
					e.preventDefault();
				}
			});
			//If width is more than 943px dropdowns are displayed on hover

			$(".menu > ul > li").click(function () {
				if ($(window).width() <= 943) {
					$(this).children("ul").slideToggle(350);
				}
			});
			//If width is less or equal to 943px dropdowns are displayed on click (thanks Aman Jain from stackoverflow)

			$(".menu-mobile").click(function (e) {
				$(".menu > ul").toggleClass('show-on-mobile');
				e.preventDefault();
			});
			//when clicked on mobile-menu, normal menu is shown as a list, classic rwd menu story (thanks mwl from stackoverflow)

	//---------menu------------//

	//--------slide---------//
            $(document).ready(function() {
              var owl = $('.owl-carousel5');
              owl.owlCarousel({
                margin: 0,
                nav: true,
                loop: true,
				autoplay:true,
				autoplayTimeout:4500,
				smartSpeed:2000,
                responsive: {
                  0: {
                    items: 1
                  },
                  600: {
                    items: 1
                  },
                  1000: {
                    items: 1
                  }
                }
              })
            }) 
			$(document).ready(function() {
              var owl3 = $('.owl-carousel3');
              owl3.owlCarousel({
                margin: 22,
                nav: true,
                loop: true,
				autoplay:true,
				autoplayTimeout:3000,
                responsive: {
                  0: {
                    items: 2
                  },
                  600: {
                    items: 4
                  },
                  1000: {
                    items: 6
                  }
                }
              })
            })	
			$(document).ready(function() {
				$(".cucheck2").click(function(){
					if ($(this).prop("checked") == false) {
						$('.sipaddres').slideUp();
					} else if ($(this).prop("checked") == true) {
						$('.sipaddres').slideDown();
					}
				});
				$(".cucheck1").click(function(){
					if ($(this).prop("checked") == false) {
						$('.dchpass').slideUp();
					} else if ($(this).prop("checked") == true) {
						$('.dchpass').slideDown();
					}
				});
			});
$(document).ready(function() {
              var owl9 = $('.owl-carousel9');
              owl9.owlCarousel({
                margin: 20,
                nav: true,
                loop: true,
				autoplay:true,
				autoplayTimeout:3000,
                responsive: {
                  0: {
                    items: 2
                  },
                  600: {
                    items: 5
                  },
                  1000: {
                    items: 7
                  }
                }
              })
            })			
	//------------slide---------//
	$(document).ready(function() {
		$(".mfilt-btn").click(function(){
			$(".sidebar").addClass("opfixed");
		});	
		$(".sclos-btn").click(function(){
			$(".sidebar").removeClass("opfixed");
		});
	});
	$(document).ready(function(){
	var quantitiy=0;
	   $('.quantity-right-plus').click(function(e){
			
			// Stop acting like a button 
			e.preventDefault();
			// Get the field name
			var quantity = parseInt($('#quantity').val()); 
							
				$('#quantity').val(quantity + 1);
			  			
		});

		 $('.quantity-left-minus').click(function(e){
			// Stop acting like a button
			e.preventDefault();
			// Get the field name
			var quantity = parseInt($('#quantity').val());
			
			// If is not undefined
		  
				// Increment
				if(quantity>0){
					$('#quantity').val(quantity - 1);
				}
		});
		
	});