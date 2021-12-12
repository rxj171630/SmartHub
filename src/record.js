import {Button} from 'semantic-ui-react'
import React from 'react'

class RecordComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      error: null,
      isLoaded: false,
      items: [],
      recording: false
    };
  }

  processResult(result) {
      if (!result) {
          console.log(result);
          return;
      } else {
          var res = []
          result.articles.forEach(function (item, index) {
            res.push({header: item.summary, meta: item.start.date})
          });
          return res.slice(0, 4);
      }
  }

  handleRecord() {
    // if (this.state.recording) {
    //     fetch("http://127.0.0.1:8000/recordEnd", {"Access-Control-Allow-Origin": "*"}).then(
    //       (result) => {
    //         console.log("end");
    //       },
    //       (error) => {
    //         console.log(error);
    //       }
    //     )
    //     this.setState({recording: false});
    // } else {
    fetch("http://127.0.0.1:8000/recordStart", {"Access-Control-Allow-Origin": "*"}).then(
      (result) => {
        console.log("start");
      },
      (error) => {
        console.log(error);
      }
    )
    this.setState({recording: true});
    // }
  }

  render() {
      console.log(this.state)
      return (
          <button class="ui button" onClick={this.handleRecord}>Record</button>
      );
  }
}

export default RecordComponent
