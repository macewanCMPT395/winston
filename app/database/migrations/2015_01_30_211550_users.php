<?php

use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;

class Users extends Migration {

	/**
	 * Run the migrations.
	 *
	 * @return void
	 */
	public function up()
	{
		//Create users table
		Schema::create('users', function(Blueprint $table)
		{
		    $table->increments('id');
		    $table->string('username')->unique();
		    $table->string('email')->unique();
		    $table->string('password');
		    $table->string('fname');
		    $table->string('lname');
		    $table->timestamps(); //created_at, updated_at timestamps
    	});
    }
   

	/**
	 * Reverse the migrations.
	 *
	 * @return void
	 */
	public function down()
	{
		// Remove users table
		Schema::drop('users');
	}

}
