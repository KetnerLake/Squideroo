/*
 * Section
 */

const section = document.querySelector( 'ink-section' );

/*
 * Setup
 */ 

setInterval( () => {
  section.animate( [
    {rotate: '360deg'}
  ], {
    duration: 500
  } );
}, 3000 );
