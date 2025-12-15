"use strict";
figma.showUI(__html__, { width: 500, height: 600 });
figma.ui.onmessage = async (msg) => {
    if (msg.type === 'generate-code') {
        const selection = figma.currentPage.selection;
        if (selection.length === 0) {
            figma.notify('Please select something first');
            return;
        }
        const simplifiedNodes = selection.map(node => serializeNode(node));
        figma.ui.postMessage({ type: 'generated-code', data: simplifiedNodes });
    }
};
function serializeNode(node) {
    const obj = {
        id: node.id,
        name: node.name,
        type: node.type,
        x: node.x,
        y: node.y,
        width: node.width,
        height: node.height,
    };
    const n = node;
    if ('fills' in node && n.fills !== figma.mixed) {
        obj.fills = n.fills;
    }
    if ('strokes' in node && n.strokes !== figma.mixed) {
        obj.strokes = n.strokes;
    }
    if ('characters' in node) {
        obj.characters = n.characters;
        obj.fontSize = n.fontSize; // Important for heuristic detection
    }
    if ('children' in node) {
        obj.children = n.children.map((child) => serializeNode(child));
    }
    if ('cornerRadius' in node && node.cornerRadius !== figma.mixed) {
        obj.cornerRadius = node.cornerRadius;
    }
    if ('strokeWeight' in node && node.strokeWeight !== figma.mixed) {
        obj.strokeWeight = node.strokeWeight;
    }
    if ('opacity' in node) {
        obj.opacity = node.opacity;
    }
    // Layout properties for Auto Layout
    if ('layoutMode' in node) {
        obj.layoutMode = n.layoutMode;
        obj.primaryAxisSizingMode = n.primaryAxisSizingMode;
        obj.counterAxisSizingMode = n.counterAxisSizingMode;
        obj.primaryAxisAlignItems = n.primaryAxisAlignItems;
        obj.counterAxisAlignItems = n.counterAxisAlignItems;
        obj.paddingLeft = n.paddingLeft;
        obj.paddingRight = n.paddingRight;
        obj.paddingTop = n.paddingTop;
        obj.paddingBottom = n.paddingBottom;
        obj.itemSpacing = n.itemSpacing;
        // Responsive Layout Props
        obj.layoutSizingHorizontal = n.layoutSizingHorizontal;
        obj.layoutSizingVertical = n.layoutSizingVertical;
    }
    return obj;
}
