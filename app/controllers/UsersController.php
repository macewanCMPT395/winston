<?php
// UsersController functions that dealt with REST behaviors
class UsersController extends \BaseController {

    public function index() {
        $users = User::all();
    
        return View::make('users.index', ['users' => $users]);
    }
    
    // When you click the username of a user in the existing database, it shows a greeting
    public function show($username) {
        $user = User::whereUsername($username)->first();
        
        return View::make('users.show', ['user' => $user]);
    }
    
    public function create() {
        return View::make('users.create');
    }
    // something wrong with carrying $users information and to populate the forms from Form::model binding
    public function edit($id) {
    
        $user = User::find($id);
        
        if(is_null($user))
        {
            return Redirect::route('users.index');
        }
            
        return View::make('users.edit', ['user' => $user]);
    }
    
    // Update user fields that already exist in the database
    public function update($id)
    {
        // grab user as well as perform validation check to make sure data is okay
        $user = User::find($id);
        $validation = Validator::make(Input::all(), ['username' => 'required', 'email' => 'required', 'password' => 'required', 'fname' => 'required', 'lname' => 'required']);

        if($validation->passes())
        {
            $user->id = Input::get('id');
            $user->password = Input::get('password');
            $user->fname = Input::get('fname');
            $user->lname = Input::get('lname');
            
            $user ->save();
            
            return Redirect::route('users.show', $id);
        }

        return Redirect::route('users.edit', $id);
    }
    
    // Delete the user from the table
    public function destroy($id)
    {
        User::destroy($id);
        
        return Redirect::to('/user');
    }
    
    // Stores the new created user from the form data entered into the database
    public function store() {
    
        // validation function to make sure user fills out all new user information
        $validation = Validator::make(Input::all(), ['username' => 'required', 'email' => 'required', 'password' => 'required', 'fname' => 'required', 'lname' => 'required']);
        
        // if validation fails, redirect to new user page with previous input filled in
        if ($validation->fails())
        {
            return Redirect::back()->withInput()->withErrors($validation->messages());
        }
        
        // Create new user if all boxes are filled and create user is clicked
        $user = new User;
        $user->username = Input::get('username');
        $user->password = Hash::make(Input::get('password'));
        $user->email = Input::get('email');
        $user->fname = Input::get('fname');
        $user->lname = Input::get('lname');
        $user->save();
        
        
        return Redirect::route('users.index');
    }
}
