<?php
//Sessions controller that keeps information of the user after they log in
class SessionsController extends \BaseController {

    // Ask user to input login, if correct brings them back to the main page
    public function create()
    {
        //if (Auth::check()) return Redirect::to('/');
        return View::make('sessions.create');
    }
    
    // Attempt user authorization
    public function store()
    {
        if (Auth::attempt(Input::only('username', 'password')))
        {
            return Redirect::route('sessions.create');	
        }
        // Brings user back to sign in page with previous input if validation fails
        return Redirect::back()->withInput();
    }
    
    // Destroys the user session
    public function destroy()
    {
        if (Auth::attempt(Input::only('username', 'password')))
        {
            Auth::logout();
        }
        return Redirect::route('sessions.create');
    }
        
}
