import {Form, Button} from 'semantic-ui-react'
import React from 'react'

class MapsComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      error: null,
      isLoaded: false,
      items: [],
      src: "",
      dst: "",
      dist: "",
      dur: ""
    };
  }

  handleChange = (e, { name, value }) => this.setState({ [name]: value })

  handleSubmit = () => {
    fetch(`http://192.168.86.41:8000/maps?src=${this.state.src}&dst=${this.state.dst}`)
      .then(res => res.json())
      .then(
        (result) => {
          console.log(result)
          this.setState({
            dur: result.rows[0].elements[0].duration.text,
            dist: result.rows[0].elements[0].distance.text,
          });
        },
        (error) => {
          this.setState({
            isLoaded: true,
            error: error
          });
        }
      )
  }

  render() {
      return (
          <div>
          <Form onSubmit={this.handleSubmit}>
          <Form.Group>
              <Form.Input
                placeholder='Source'
                name='src'
                onChange={this.handleChange}
              />
              <Form.Input
                placeholder='Destination'
                name='dst'
                onChange={this.handleChange}
              />
              <Form.Button content='Submit' />
        </Form.Group>
        </Form>
        <div>Distance: {this.state.dist}</div>
        <div>Duration: {this.state.dur}</div>
        </div>
      );
  }
}

export default MapsComponent
