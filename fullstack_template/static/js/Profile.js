import React from "react"

export default class Profile extends React.Component {


render () {
    var data = 	[
    				{
    					"name": "James Angus",
    					"age" : "22",
    					"job": "Dentist"
    				},
    				{
    					"name": "Milan Howen",
    					"age" : "36",
    					"job": "Truck Driver"
    				}
    			];
    return (
            <form onSubmit={this.handleSubmit}>
                <h1>
                    <label>Rajshree Chauhan</label> <a href="#" class="btn btn-info btn-lg">
                                                              <span class="glyphicon glyphicon-pencil"></span> Edit Profile
                                                            </a><br />
                    <label>Email: chauhan.shree@gmail.com</label><br />
                    <label>Phone: 9253298611</label><br />
                    <label>Biography: Life</label>
                </h1>




            </form>
    );
  }
}