from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.users.manager import user_manager
from app.vpn.manager import vpn_manager
from app.vpn.wireguard import (
    wireguard_manager
)


router = APIRouter(
    prefix="/v1"
)


class CreateUserRequest(BaseModel):

    name: str


class CreatePeerRequest(BaseModel):

    user_id: str

    name: str


@router.get("/status")
def status():

    return {
        "success": True,
        "service": "AniVora VPN",
        "status": "online"
    }


@router.get("/wireguard")
def wireguard_status():

    return {
        "success": True,
        "wireguard": (
            wireguard_manager.status()
        )
    }


@router.post("/users")
def create_user(
    request: CreateUserRequest
):

    if not request.name.strip():

        raise HTTPException(
            status_code=400,
            detail="User name cannot be empty"
        )

    user = user_manager.create_user(
        request.name
    )

    return {
        "success": True,
        "user": user
    }


@router.get("/users")
def list_users():

    return {
        "success": True,
        "users": user_manager.list_users()
    }


@router.get("/users/{user_id}")
def get_user(user_id: str):

    user = user_manager.get_user(
        user_id
    )

    if not user:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "success": True,
        "user": user
    }


@router.delete("/users/{user_id}")
def delete_user(user_id: str):

    deleted = user_manager.delete_user(
        user_id
    )

    if not deleted:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "success": True,
        "deleted": True
    }


@router.post("/peers")
def create_peer(
    request: CreatePeerRequest
):

    user = user_manager.get_user(
        request.user_id
    )

    if not user:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    if not request.name.strip():

        raise HTTPException(
            status_code=400,
            detail="Peer name cannot be empty"
        )

    peer = vpn_manager.create_peer(
        request.user_id,
        request.name
    )

    return {
        "success": True,
        "peer": peer
    }


@router.get("/peers")
def list_peers():

    return {
        "success": True,
        "peers": vpn_manager.list_peers()
    }


@router.get("/peers/{peer_id}")
def get_peer(peer_id: str):

    peer = vpn_manager.get_peer(
        peer_id
    )

    if not peer:

        raise HTTPException(
            status_code=404,
            detail="Peer not found"
        )

    return {
        "success": True,
        "peer": peer
    }


@router.post("/peers/{peer_id}/connect")
def connect_peer(peer_id: str):

    peer = vpn_manager.connect_peer(
        peer_id
    )

    if not peer:

        raise HTTPException(
            status_code=404,
            detail="Peer not found"
        )

    return {
        "success": True,
        "peer": peer
    }


@router.post("/peers/{peer_id}/disconnect")
def disconnect_peer(peer_id: str):

    peer = vpn_manager.disconnect_peer(
        peer_id
    )

    if not peer:

        raise HTTPException(
            status_code=404,
            detail="Peer not found"
        )

    return {
        "success": True,
        "peer": peer
    }


@router.delete("/peers/{peer_id}")
def delete_peer(peer_id: str):

    deleted = vpn_manager.delete_peer(
        peer_id
    )

    if not deleted:

        raise HTTPException(
            status_code=404,
            detail="Peer not found"
        )

    return {
        "success": True,
        "deleted": True
    }
