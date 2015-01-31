@extends('layouts.recipe')

@section('content')

    <h1><u>Healthy Foods Recipe Library</u></h1>
    <br><br>
    <div id="tabitem">
    <ul>
      <li>Recipe #1</li>
      <li>Recipe #2</li>
      <li>Recipe #3</li>
      <li>Recipe #4</li>
      <li>Recipe #5</li>
      <li>Recipe #6</li>
      <li>Recipe #8</li>
      <li>Recipe #9</li>
      <li>Recipe #10</li> 
    </ul>
    </div>

    <div id="items">
    <p><h2> Take a look at this cheesecake! </h2>
    <img src=/foodgallery/ricottacheesecake.jpg height=120 width=350>
    Only 200 calories, the secret recipe is available soon ... check back in a couple days!
    </p>
    </div>
    
    <div id="items">
    <p><h2> Do you like blueberries or strawberries? </h2>
    <img src=/foodgallery/fresh_berries.jpg height=200 width=320>
    Only 200 calories in this all natural blend of fruits. Totally throw in some bananas if you want to.
    </p>
    </div>
            
    <div id="items">
    <p><h2> Grains, Oats, Honey Wheats.. </h2>
    <img src=/foodgallery/oatmealpie.jpg height=220 width=350>
    The heartiest meal of oats yet! Lose 10 pounds in 2 weeks just by switching to a high grains diet.
    </p>
    </div>

@stop

@section('footer')

@stop
