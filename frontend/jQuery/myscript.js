$('h1').click(function(){
    console.log('check passed')
    $(this).text('This was changed')
})

// $('input').eq(0).keypress(function(){
//     $('h1').toggleClass('turnBlue')
// })

$('input').eq(0).keypress(function(event){
    $('h1').toggleClass('turnRed')
})

function changeColor(rowIndex, colIndex, color){
    return table
}