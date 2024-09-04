import { AfterViewInit, Component, OnInit } from '@angular/core';
import { BlockComponent } from '../block/block.component';
import { Block } from '../models/block';
import { BlockManagerService } from '../service/block-manager.service';
import { NavBarComponent } from '../nav-bar/nav-bar.component';
import { jsPlumbInstance } from 'jsplumb';
import { ExampleService } from '../service/example.service';
import { HttpClient } from '@angular/common/http';


interface ExampleResponse {
  message: string;
  image_data: string; // Base64 encoded image data
}


@Component({
  selector: 'app-canvas',
  standalone: true,
  imports: [BlockComponent, NavBarComponent],
  templateUrl: './canvas.component.html',
  styleUrl: './canvas.component.scss',
  providers: [HttpClient],
})


export class CanvasComponent implements OnInit, AfterViewInit {
  public numberOfBlock: number = 0;
  public blockList: Block[] = [];
  public data: string = '';

  constructor(
    private _blockManagerService: BlockManagerService,
    private exampleService: ExampleService
  ) {
    this.blockList = [...this._blockManagerService.blockList];
  }
  ngOnInit(): void {
    this.numberOfBlock = this.blockList.length;
    this._blockManagerService.$isBlockUpdateAvailable.subscribe(
      (isupdateAvailable) => {
        if (isupdateAvailable) {
          this.blockList = [...this._blockManagerService.blockList];
        }
      }
    );

    this.exampleService.getExampleData().subscribe((res: ExampleResponse) => {

      
      this.data = res.image_data;
      // in the console log it is getting printed
      console.log(this.data);


      // // Assign the image data to the first block (or create a new block)
      if (this.blockList.length > 0) {
        this.blockList[0].imagedata = this.data;
      } 
      
      // else {
      // //   const newBlock = new Block();
      // //   newBlock.imagedata = this.data;
      // //   this.blockList.push(newBlock);
      // // }

    });
  }

  public ngAfterViewInit(): void {
    const jsPlumbInstance = this._blockManagerService.getJsPlumbInstance();
    jsPlumbInstance.setContainer('example-boundary');
    console.log('AfterViewInit Called.....');

    this._blockManagerService.$isNewBlockPushed.subscribe(
      (isBlockPushed: boolean) => {
        if (isBlockPushed) {
          jsPlumbInstance.draggable(
            'control_' + this.blockList[this.blockList.length - 1].id,
            {
              containment: 'parent',
            }
          );

          this.makeConnectable(
            jsPlumbInstance,
            'control_' + this.blockList[this.blockList.length - 1].id
          );
        }
      }
    );
  }

  public makeConnectable(instance: jsPlumbInstance, elementId: any) {
    instance.makeSource(elementId, {
      filter: '.ep',
      anchor: 'Continuous',
      connectorStyle: {
        stroke: 'black',
        strokeWidth: 20,
        outlineStroke: 'transparent',
        outlineWidth: 4,
      },
      connectionType: 'basic',
    });

    instance.makeTarget(elementId, {
      anchor: 'Continuous',
      allowLoopback: false,
      paintStyle: { fill: 'black', radius: 12 },
    });

    instance.addEndpoint(elementId, {
      endpoint: 'Dot',
      anchor: ['Right', 'Left', 'Top', 'Bottom'],
      isSource: true,
      isTarget: true,
      maxConnections: 1,
      paintStyle: { fill: 'black' },
    });
  }
}
