import {Form, Button} from 'semantic-ui-react'
import React from 'react'

class AlarmComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      error: null,
      isLoaded: false,
      items: [],
      hour: "",
      minute: "",
    };
  }

  handleChange = (e, { name, value }) => this.setState({ [name]: value })

  handleSubmit = () => {
      var today = new Date();
      var currHour = today.getHours();
      var currMin = today.getMinutes();

      var currDayMin = currHour * 60 + currMin;
      var alarmMin = parseInt(this.state.hour, 10) * 60 + parseInt(this.state.minute, 10);
      console.log("curr day min: ", currDayMin);
      console.log("alarm min: ", alarmMin);

      var alarmInput = 0;
      if (alarmMin >= currDayMin) {
          alarmInput = alarmMin -  currDayMin;
      } else {
          alarmInput = (1440 - currDayMin) + alarmMin;
      }
      console.log(alarmInput);

      alert(`Set alarm at ${this.state.hour}:${this.state.minute}`);
      sleep(alarmInput).then(() => {
           fetch("http://127.0.0.1:8000/alarm").then(res => res.json())
           .then(
             (result) => {
               console.log("alarm");
             },
             (error) => {
               console.log(error);
             }
           )
      });
      //helper function for delays in JS
      function sleep (time) {
          return new Promise((resolve) => setTimeout(resolve, (time * 1000 * 60)));
      }
  }

  render() {
      return (
          <div>
          <Form onSubmit={this.handleSubmit}>
          <Form.Group>
              <Form.Input
                placeholder='Hour'
                name='hour'
                onChange={this.handleChange}
              />
              <Form.Input
                placeholder='Minute'
                name='minute'
                onChange={this.handleChange}
              />
              <Form.Button content='Set Alarm' />
        </Form.Group>
        </Form>
        </div>
      );
  }
}

export default AlarmComponent
