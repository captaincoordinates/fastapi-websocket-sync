import { Component, OnInit } from '@angular/core';
import { Observable, Observer } from 'rxjs';
import { environment } from 'src/environments/environment';
import { PushReport } from '../types/api_push_report';

@Component({
  selector: 'app-wsclient',
  templateUrl: './wsclient.component.html',
  styleUrls: ['./wsclient.component.less']
})
export class WsclientComponent implements OnInit {

  public connectReport?: PushReport;
  public updateReport?: PushReport;
  public contentVisible: boolean = false;

  private initObserver?: Observer<void> = undefined;
  private wsEndpoint: string = "";
  private websocket?: WebSocket = undefined;

  constructor() {
    this.wsEndpoint = `${window.location.protocol.replace("http", "ws")}//${environment.api_host}${environment.api_port ? ":" + environment.api_port : ""}/ws`
    console.log(`wsEndpoint: ${this.wsEndpoint}`)
    new Observable((observer) => {
      this.initObserver = observer;
    }).subscribe(() => {
      this.contentVisible = true;
    })
  }

  public ngOnInit(): void {
    this.establishWs(() => {
      if (this.initObserver) {
        this.initObserver.next();
        this.initObserver.complete();
      }
    });
  }

  public reconnectClicked(): void {
    if (this.websocket) {
      this.updateReport = undefined;
      this.websocket.onclose = () => {
        this.establishWs()
      }
      this.websocket.close()
    }
  }

  public initPushClicked(): void {
    this.sendMessage("client button clicked")
  }

  private establishWs(openHandler?: Function): void {
    this.websocket = new WebSocket(this.wsEndpoint);
    this.websocket.onopen = () => {
      if (this.websocket) {
        this.websocket.onmessage = arg => {
          this.pushReceived(arg.data);
        };
      }
      if (openHandler) {
        openHandler();
      }
    };
  }

  private sendMessage(message: string): void {
    if (this.websocket) {
      this.websocket.send(message)
    }
  }

  private pushReceived(arg: string): void {
    const parsed = JSON.parse(arg);
    switch (parsed.push_type) {
      case "connected_to":
        this.connectReport = parsed;
        break;
      case "notified_by":
        this.updateReport = parsed;
        break;
    }
  }
}
